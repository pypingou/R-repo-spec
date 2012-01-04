%global packname  stabledist
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.2.1
Release:          1%{?dist}
Summary:          Stable Distribution Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-2.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Density, Probability and Quantile functions, and random number generation
for (skew) stable distributions, using the parametrizations of Nolan.

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
%doc %{rlibdir}/stabledist/DESCRIPTION
%doc %{rlibdir}/stabledist/html
%{rlibdir}/stabledist/Meta
%{rlibdir}/stabledist/unitTests
%{rlibdir}/stabledist/R
%{rlibdir}/stabledist/NAMESPACE
%{rlibdir}/stabledist/help
%{rlibdir}/stabledist/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2.1-1
- initial package for Fedora