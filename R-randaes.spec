%global packname  randaes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{dist}
Summary:          Random number generator based on AES cipher

Group:            Applications/Engineering 
License:          GPL 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The deterministic part of the Fortuna cryptographic pseudorandom number
generator, described by Scheier & Ferguson "Practical  Cryptography"

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
%doc %{rlibdir}/randaes/DESCRIPTION
%doc %{rlibdir}/randaes/html
%{rlibdir}/randaes/help
%{rlibdir}/randaes/INDEX
%{rlibdir}/randaes/Meta
%{rlibdir}/randaes/libs
%{rlibdir}/randaes/R
%{rlibdir}/randaes/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- Update to version 0.3

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora