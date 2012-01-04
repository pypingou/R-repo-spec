%global packname  xpose4data
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.3.2
Release:          1%{?dist}
Summary:          Xpose 4 Data Functions Package

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-Hmisc R-gam R-methods 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-Hmisc R-gam R-methods 

%description
Xpose is collection of packages to be used as a model building aid for
non-linear mixed effects (population) analysis using NONMEM. It
facilitates data set checkout, exploration and visualization, model
diagnostics, candidate covariate identification and model comparison.
xpose4data is a package containing functions for reading in data from
NONMEM, support functions, as well as class definitions.

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
%doc %{rlibdir}/xpose4data/CITATION
%doc %{rlibdir}/xpose4data/DESCRIPTION
%doc %{rlibdir}/xpose4data/html
%{rlibdir}/xpose4data/readme.txt
%{rlibdir}/xpose4data/INDEX
%{rlibdir}/xpose4data/NAMESPACE
%{rlibdir}/xpose4data/Meta
%{rlibdir}/xpose4data/xpose.ini
%{rlibdir}/xpose4data/R
%{rlibdir}/xpose4data/changelog.txt
%{rlibdir}/xpose4data/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.3.2-1
- initial package for Fedora