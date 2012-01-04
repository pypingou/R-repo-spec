%global packname  rjson
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          JSON for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Converts R object into JSON objects and vice-versa

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
%doc %{rlibdir}/rjson/doc
%doc %{rlibdir}/rjson/html
%doc %{rlibdir}/rjson/DESCRIPTION
%{rlibdir}/rjson/rpc_server
%{rlibdir}/rjson/unittests
%{rlibdir}/rjson/Meta
%{rlibdir}/rjson/INDEX
%{rlibdir}/rjson/R
%{rlibdir}/rjson/libs
%{rlibdir}/rjson/help
%{rlibdir}/rjson/changelog.txt
%{rlibdir}/rjson/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora