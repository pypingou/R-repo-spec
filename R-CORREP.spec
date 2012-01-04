%global packname  CORREP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Multivariate Correlation Estimator and Statistical Inference Procedures.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-e1071 R-stats 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-e1071 R-stats 


%description
Multivariate correlation estimation and statistical inference. See package

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
%doc %{rlibdir}/CORREP/doc
%doc %{rlibdir}/CORREP/DESCRIPTION
%doc %{rlibdir}/CORREP/html
%{rlibdir}/CORREP/NAMESPACE
%{rlibdir}/CORREP/INDEX
%{rlibdir}/CORREP/help
%{rlibdir}/CORREP/Meta
%{rlibdir}/CORREP/data
%{rlibdir}/CORREP/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora