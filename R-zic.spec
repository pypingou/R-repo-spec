%global packname  zic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          Bayesian Inference for Zero-Inflated Count Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides MCMC algorithms for the analysis of zero-inflated
count models. The case of stochastic search variable selection (SSVS) is
also considered. All MCMC samplers are coded in C++ for improved
efficiency. A data set considering the demand for health care is also

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
%doc %{rlibdir}/zic/html
%doc %{rlibdir}/zic/DESCRIPTION
%{rlibdir}/zic/R
%{rlibdir}/zic/libs
%{rlibdir}/zic/data
%{rlibdir}/zic/NAMESPACE
%{rlibdir}/zic/INDEX
%{rlibdir}/zic/Meta
%{rlibdir}/zic/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.4-1
- initial package for Fedora