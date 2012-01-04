%global packname  PoiClaClu
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Classification and clustering of sequencing data based on a Poisson model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implements the methods described in the paper, Witten (2011)
Classification and Clustering of Sequencing Data using a Poisson Model, to
appear in Annals of Applied Statistics.

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
%doc %{rlibdir}/PoiClaClu/DESCRIPTION
%doc %{rlibdir}/PoiClaClu/html
%{rlibdir}/PoiClaClu/INDEX
%{rlibdir}/PoiClaClu/NAMESPACE
%{rlibdir}/PoiClaClu/help
%{rlibdir}/PoiClaClu/R
%{rlibdir}/PoiClaClu/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora