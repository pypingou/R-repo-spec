%global packname  PKgraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Model diagnostics for population pharmacokinetic models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RGtk2 R-gWidgetsRGtk2 R-cairoDevice R-lattice R-rggobi R-ggplot2 

BuildRequires:    R-devel tex(latex) R-RGtk2 R-gWidgetsRGtk2 R-cairoDevice R-lattice R-rggobi R-ggplot2 

%description
PKgraph provides a graphical user interface for population pharmacokinetic
model diagnosis. It also provides an integrated and comprehensive platform
for the analysis of pharmacokinetic data including exploratory data
analysis, goodness of model fit, model validation and model comparison.
Results from a variety of modeling fitting software, including NONMEM,
Monolix, SAS and R, can be used. PKgraph is programmed in R, and uses the
R packages lattice, ggplot2 for static graphics, and rggobi for
interactive graphics.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora