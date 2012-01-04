%global packname  clusterRepro
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1.1
Release:          1%{?dist}
Summary:          Reproducibility of gene expression clusters

Group:            Applications/Engineering 
License:          GPL 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-1.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A function for validating microarry clusters via reproducibility

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
%doc %{rlibdir}/clusterRepro/html
%doc %{rlibdir}/clusterRepro/DESCRIPTION
%{rlibdir}/clusterRepro/R
%{rlibdir}/clusterRepro/NAMESPACE
%{rlibdir}/clusterRepro/help
%{rlibdir}/clusterRepro/INDEX
%{rlibdir}/clusterRepro/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1.1-1
- initial package for Fedora