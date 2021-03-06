%global packname  fame
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.18
Release:          1%{dist}
Summary:          Interface for FAME time series database

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tis 

BuildRequires:    R-devel tex(latex) R-tis 

%description
Read and write FAME databases.

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
%doc %{rlibdir}/fame/DESCRIPTION
%doc %{rlibdir}/fame/html
%doc %{rlibdir}/fame/NEWS
%{rlibdir}/fame/help
%{rlibdir}/fame/README
%{rlibdir}/fame/Meta
%{rlibdir}/fame/libs
%{rlibdir}/fame/R
%{rlibdir}/fame/NAMESPACE
%{rlibdir}/fame/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.18-1
- Update to version 2.18

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.17-1
- initial package for Fedora