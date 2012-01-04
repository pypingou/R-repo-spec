%global packname  filehash
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Simple key-value database

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Simple key-value database

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
%doc %{rlibdir}/filehash/CITATION
%doc %{rlibdir}/filehash/doc
%doc %{rlibdir}/filehash/DESCRIPTION
%doc %{rlibdir}/filehash/NEWS
%doc %{rlibdir}/filehash/COPYING
%doc %{rlibdir}/filehash/html
%{rlibdir}/filehash/R
%{rlibdir}/filehash/NAMESPACE
%{rlibdir}/filehash/libs
%{rlibdir}/filehash/Meta
%{rlibdir}/filehash/help
%{rlibdir}/filehash/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora