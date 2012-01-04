%global packname  QSARdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Quantitative Structure Activity Relationship (QSAR) Data Sets

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Molecular descriptors and outcomes for several public domain data sets

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
%doc %{rlibdir}/QSARdata/html
%doc %{rlibdir}/QSARdata/DESCRIPTION
%{rlibdir}/QSARdata/INDEX
%{rlibdir}/QSARdata/Meta
%{rlibdir}/QSARdata/NAMESPACE
%{rlibdir}/QSARdata/data
%{rlibdir}/QSARdata/R
%{rlibdir}/QSARdata/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora