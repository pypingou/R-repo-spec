%global packname  MaXact
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Exact max-type Cochran-Armitage trend test(CATT)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mnormt 

BuildRequires:    R-devel tex(latex) R-mnormt 

%description
Perform exact MAX3 or MAX2 test for one-locus genetic association analysis
and trend test for dominant, recessive and additive models. It can also
calculate approximated p-value with the normal approximation method.

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
%doc %{rlibdir}/MaXact/html
%doc %{rlibdir}/MaXact/DESCRIPTION
%{rlibdir}/MaXact/Meta
%{rlibdir}/MaXact/libs
%{rlibdir}/MaXact/NAMESPACE
%{rlibdir}/MaXact/R
%{rlibdir}/MaXact/INDEX
%{rlibdir}/MaXact/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora