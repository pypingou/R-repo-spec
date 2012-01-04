%global packname  R2STATS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.68.27
Release:          1%{?dist}
Summary:          A GTK GUI for fitting and comparing GLM and GLMM in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.68-27.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-proto R-cairoDevice R-gWidgetsRGtk2 R-MASS R-RGtk2Extras R-latticeExtra 
Requires:         R-Matrix R-lme4 R-utils 

BuildRequires:    R-devel tex(latex) R-proto R-cairoDevice R-gWidgetsRGtk2 R-MASS R-RGtk2Extras R-latticeExtra
BuildRequires:    R-Matrix R-lme4 R-utils 


%description
R2STATS is a gWidgetsRGtk2 GUI for fitting and comparing GLM or GLMM
(based on Douglas Bates' lme4 package) in R. It is designed to make
comparisons between numerous models easy, both numerically and
graphically, which may be useful for teaching. Relevant plots are
automatically produced for each model family. R2STATS is *not* a generic
graphical interface for R, but a GUI for statistical modelling in a model
comparison approach.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.68.27-1
- initial package for Fedora