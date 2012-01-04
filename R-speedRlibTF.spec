%global packname  speedRlibTF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.30
Release:          1%{?dist}
Summary:          speedR's table filter library

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-30.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains the library "tablefilter", which is used by speedR.

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
%doc %{rlibdir}/speedRlibTF/html
%doc %{rlibdir}/speedRlibTF/DESCRIPTION
%{rlibdir}/speedRlibTF/R
%{rlibdir}/speedRlibTF/INDEX
%{rlibdir}/speedRlibTF/java
%{rlibdir}/speedRlibTF/help
%{rlibdir}/speedRlibTF/NAMESPACE
%{rlibdir}/speedRlibTF/Meta
%{rlibdir}/speedRlibTF/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.30-1
- initial package for Fedora