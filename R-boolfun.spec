%global packname  boolfun
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Cryptographic Boolean Functions

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
This package can be used to assess cryptographic properties of Boolean
functions such as nonlinearity, algebraic immunity, resiliency, etc... It
also implements functionality to handle Boolean polynomials, namely
multiplication and addition of multivariate polynomials with coefficients
and exponents in \{0,1\}.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora