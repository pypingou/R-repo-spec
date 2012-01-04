%global packname  RSAGA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.92.2
Release:          1%{?dist}
Summary:          SAGA Geoprocessing and Terrain Analysis in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.92-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
RSAGA provides access to geocomputing and terrain analysis functions of
SAGA from within R by running the command line version of SAGA. In
addition, several R functions for handling and manipulating ASCII grids
are provided, including a flexible framework for applying local functions
(including predict methods of fitted models) or focal functions to
multiple grids. SAGA is available under GPL via

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
%doc %{rlibdir}/RSAGA/html
%doc %{rlibdir}/RSAGA/DESCRIPTION
%{rlibdir}/RSAGA/help
%{rlibdir}/RSAGA/INDEX
%{rlibdir}/RSAGA/Meta
%{rlibdir}/RSAGA/NAMESPACE
%{rlibdir}/RSAGA/R

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.92.2-1
- initial package for Fedora