%global packname  mecdf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Multivariate Empirical Cumulative Distribution Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-s3x 

BuildRequires:    R-devel tex(latex) R-s3x 

%description
Multivariate empirical cumulative distribution functions, including both
step functions and continuous functions.

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
%doc %{rlibdir}/mecdf/html
%doc %{rlibdir}/mecdf/DESCRIPTION
%doc %{rlibdir}/mecdf/doc
%{rlibdir}/mecdf/INDEX
%{rlibdir}/mecdf/Meta
%{rlibdir}/mecdf/R
%{rlibdir}/mecdf/help
%{rlibdir}/mecdf/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora