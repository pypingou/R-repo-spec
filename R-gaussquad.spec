%global packname  gaussquad
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Collection of functions for Gaussian quadrature

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-polynom R-orthopolynom 

BuildRequires:    R-devel tex(latex) R-polynom R-orthopolynom 

%description
A collection of functions to perform Gaussian quadrature with different
weight functions corresponding to the orthogonal polynomials in package
orthopolynom.  Examples verify the orthogonality and inner products of the

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
%doc %{rlibdir}/gaussquad/html
%doc %{rlibdir}/gaussquad/DESCRIPTION
%{rlibdir}/gaussquad/NAMESPACE
%{rlibdir}/gaussquad/R
%{rlibdir}/gaussquad/help
%{rlibdir}/gaussquad/INDEX
%{rlibdir}/gaussquad/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora