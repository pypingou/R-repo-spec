%global packname  ORCME
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{dist}
Summary:          Order Restricted Clustering for Microarray Experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides clustering of genes with similar dose response (or
time course) profiles. It implements the method described by Lin et al.

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
%doc %{rlibdir}/ORCME/DESCRIPTION
%doc %{rlibdir}/ORCME/NEWS
%doc %{rlibdir}/ORCME/html
%{rlibdir}/ORCME/NAMESPACE
%{rlibdir}/ORCME/Meta
%{rlibdir}/ORCME/INDEX
%{rlibdir}/ORCME/R
%{rlibdir}/ORCME/help
%{rlibdir}/ORCME/data

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- Update to version 1.1

* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora