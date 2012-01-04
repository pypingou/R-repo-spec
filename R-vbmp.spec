%global packname  vbmp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Variational Bayesian Multinomial Probit Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Variational Bayesian Multinomial Probit Regression with Gaussian Process
Priors. It estimates class membership posterior probability employing
variational and sparse approximation to the full posterior. This software
also incorporates feature weighting by means of Automatic Relevance

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
%doc %{rlibdir}/vbmp/html
%doc %{rlibdir}/vbmp/doc
%doc %{rlibdir}/vbmp/DESCRIPTION
%{rlibdir}/vbmp/help
%{rlibdir}/vbmp/INDEX
%{rlibdir}/vbmp/Meta
%{rlibdir}/vbmp/NAMESPACE
%{rlibdir}/vbmp/R
%{rlibdir}/vbmp/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora