%global packname  flip
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Multivariate Permutation Tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-foreach R-e1071 R-someMTP 

BuildRequires:    R-devel tex(latex) R-methods R-foreach R-e1071 R-someMTP 

%description
It implements univariate and multivariate permutation test, also allowing
multiplicity control.

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
%doc %{rlibdir}/flip/html
%doc %{rlibdir}/flip/DESCRIPTION
%{rlibdir}/flip/NAMESPACE
%{rlibdir}/flip/help
%{rlibdir}/flip/Meta
%{rlibdir}/flip/INDEX
%{rlibdir}/flip/R

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora