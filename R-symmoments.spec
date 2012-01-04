%global packname  symmoments
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Symbolic Central Moments of the Multivariate Normal Distribution

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Symbolic central moments of the multivariate normal distribution. Computes
a standard representation, LateX code, and values at specified covariance

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
%doc %{rlibdir}/symmoments/doc
%doc %{rlibdir}/symmoments/DESCRIPTION
%doc %{rlibdir}/symmoments/html
%doc %{rlibdir}/symmoments/CITATION
%{rlibdir}/symmoments/help
%{rlibdir}/symmoments/NAMESPACE
%{rlibdir}/symmoments/R
%{rlibdir}/symmoments/INDEX
%{rlibdir}/symmoments/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora