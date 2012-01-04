%global packname  xpose4generic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.3.3
Release:          1%{?dist}
Summary:          Xpose 4 Generic Functions Package

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data 

%description
Xpose is collection of packages to be used as a model building aid for
non-linear mixed effects (population) analysis using NONMEM. It
facilitates data set checkout, exploration and visualization, model
diagnostics, candidate covariate identification and model comparison.
xpose4generic is a package containing generic functions for plotting, as
well as class definitions.  Highly customizeable, but requires more user
input that xpose4specific.

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
%doc %{rlibdir}/xpose4generic/DESCRIPTION
%doc %{rlibdir}/xpose4generic/html
%doc %{rlibdir}/xpose4generic/CITATION
%{rlibdir}/xpose4generic/R
%{rlibdir}/xpose4generic/changelog.txt
%{rlibdir}/xpose4generic/INDEX
%{rlibdir}/xpose4generic/readme.txt
%{rlibdir}/xpose4generic/Meta
%{rlibdir}/xpose4generic/NAMESPACE
%{rlibdir}/xpose4generic/help

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.3.3-1
- initial package for Fedora