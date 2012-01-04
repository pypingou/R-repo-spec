%global packname  identity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Jacquard Condensed Coefficients of Identity

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Calculate identity coefficients, based on Mark Abney's C code.

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
%doc %{rlibdir}/identity/html
%doc %{rlibdir}/identity/DESCRIPTION
%{rlibdir}/identity/R
%{rlibdir}/identity/libs
%{rlibdir}/identity/INDEX
%{rlibdir}/identity/NAMESPACE
%{rlibdir}/identity/help
%{rlibdir}/identity/Meta
%{rlibdir}/identity/example

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora