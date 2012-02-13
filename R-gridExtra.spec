%global packname  gridExtra
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{dist}
Summary:          functions in Grid graphics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
misc. high-level Grid functions

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
%doc %{rlibdir}/gridExtra/html
%doc %{rlibdir}/gridExtra/NEWS
%doc %{rlibdir}/gridExtra/DESCRIPTION
%{rlibdir}/gridExtra/INDEX
%{rlibdir}/gridExtra/Meta
%{rlibdir}/gridExtra/NAMESPACE
%{rlibdir}/gridExtra/tableGrob2.r
%{rlibdir}/gridExtra/R
%{rlibdir}/gridExtra/help
%{rlibdir}/gridExtra/test

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- Update to version 0.8.1

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.5-1
- initial package for Fedora