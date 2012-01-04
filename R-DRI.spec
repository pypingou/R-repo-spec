%global packname  DRI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          DR-Integrator

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-impute R-cghFLasso 

BuildRequires:    R-devel tex(latex) R-impute R-cghFLasso 

%description
Integrative analysis of DNA copy number and gene expression data described
in Salari et al 2009

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
%doc %{rlibdir}/DRI/html
%doc %{rlibdir}/DRI/DESCRIPTION
%{rlibdir}/DRI/R
%{rlibdir}/DRI/Meta
%{rlibdir}/DRI/NAMESPACE
%{rlibdir}/DRI/help
%{rlibdir}/DRI/data
%{rlibdir}/DRI/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora