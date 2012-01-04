%global packname  doMC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Foreach parallel adaptor for the multicore package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreach R-iterators R-multicore R-utils 

BuildRequires:    R-devel tex(latex) R-foreach R-iterators R-multicore R-utils 

%description
Provides a parallel backend for the %dopar% function using Simon Urbanek's
multicore package.

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora