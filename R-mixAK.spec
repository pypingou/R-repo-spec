%global packname  mixAK
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Mixture of methods including mixtures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-colorspace R-lme4 R-mnormt R-coda 


BuildRequires:    R-devel tex(latex) R-splines R-colorspace R-lme4 R-mnormt R-coda



%description
This package contains a mixture of statistical methods including the MCMC
methods to analyze normal mixtures

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
%doc %{rlibdir}/mixAK/html
%doc %{rlibdir}/mixAK/DESCRIPTION
%doc %{rlibdir}/mixAK/CITATION
%doc %{rlibdir}/mixAK/doc
%{rlibdir}/mixAK/libs
%{rlibdir}/mixAK/Meta
%{rlibdir}/mixAK/INDEX
%{rlibdir}/mixAK/data
%{rlibdir}/mixAK/NAMESPACE
%{rlibdir}/mixAK/R
%{rlibdir}/mixAK/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora