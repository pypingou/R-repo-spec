%global packname  simctest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.99
Release:          1%{?dist}
Summary:          Safe implementation of Monte Carlo tests.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
Monte Carlo computation of p-value with uniformly bounded resampling risk,
computation of the power of a Monte test.

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
%doc %{rlibdir}/simctest/CITATION
%doc %{rlibdir}/simctest/doc
%doc %{rlibdir}/simctest/DESCRIPTION
%doc %{rlibdir}/simctest/html
%{rlibdir}/simctest/Meta
%{rlibdir}/simctest/help
%{rlibdir}/simctest/libs
%{rlibdir}/simctest/INDEX
%{rlibdir}/simctest/R
%{rlibdir}/simctest/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.99-1
- initial package for Fedora