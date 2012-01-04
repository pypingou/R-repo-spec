%global packname  bimetallic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Power for SNP analyses using silver standard cases

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A power calculator for Genome-wide association studies (GWAs) with
combined gold (error-free) and silver (erroneous) phenotyping per McDavid
A, Crane PK, Newton KM, Crosslin DR, et al. (2011)

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
%doc %{rlibdir}/bimetallic/DESCRIPTION
%doc %{rlibdir}/bimetallic/html
%{rlibdir}/bimetallic/R
%{rlibdir}/bimetallic/Meta
%{rlibdir}/bimetallic/help
%{rlibdir}/bimetallic/INDEX
%{rlibdir}/bimetallic/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora