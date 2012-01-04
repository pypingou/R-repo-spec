%global packname  lqa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Penalized Likelihood Inference for GLMs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides some basic infrastructure and tools to fit
Generalized Linear Models (GLMs) via penalized likelihood inference.
Estimating procedures already implemented are the LQA algorithm (that is
where its name come from), P-IRLS, RidgeBoost, GBlockBoost and

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
%doc %{rlibdir}/lqa/doc
%doc %{rlibdir}/lqa/html
%doc %{rlibdir}/lqa/DESCRIPTION
%{rlibdir}/lqa/Meta
%{rlibdir}/lqa/INDEX
%{rlibdir}/lqa/R
%{rlibdir}/lqa/NAMESPACE
%{rlibdir}/lqa/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora