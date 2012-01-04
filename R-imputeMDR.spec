%global packname  imputeMDR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          The Multifactor Dimensionality Reduction (MDR) Analysis for Imcomplete Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides various approaches to handling missing values for
the MDR analysis to identify gene-gene interactions using biallelic marker
data in genetic association studies

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
%doc %{rlibdir}/imputeMDR/DESCRIPTION
%doc %{rlibdir}/imputeMDR/html
%{rlibdir}/imputeMDR/NAMESPACE
%{rlibdir}/imputeMDR/INDEX
%{rlibdir}/imputeMDR/help
%{rlibdir}/imputeMDR/Meta
%{rlibdir}/imputeMDR/data
%{rlibdir}/imputeMDR/R
%{rlibdir}/imputeMDR/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora