%global packname  marg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Approximate marginal inference for regression-scale models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-statmod R-survival 


BuildRequires:    R-devel tex(latex) R-statmod R-survival



%description
Likelihood inference based on higher order approximations for linear
nonnormal regression models

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
%doc %{rlibdir}/marg/CITATION
%doc %{rlibdir}/marg/LICENCE
%doc %{rlibdir}/marg/html
%doc %{rlibdir}/marg/doc
%doc %{rlibdir}/marg/DESCRIPTION
%{rlibdir}/marg/INDEX
%{rlibdir}/marg/Meta
%{rlibdir}/marg/NAMESPACE
%{rlibdir}/marg/R
%{rlibdir}/marg/data
%{rlibdir}/marg/margdemo.R
%{rlibdir}/marg/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora