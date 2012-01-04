%global packname  MAINT.Data
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Model and Analize Interval Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-sn R-methods R-miscTools 

BuildRequires:    R-devel tex(latex) R-MASS R-sn R-methods R-miscTools 

%description
MAINT.Data implements methodologies for modelling Interval Data,
considering five different possible configurations structures for the
variance-covariance matrix.

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
%doc %{rlibdir}/MAINT.Data/DESCRIPTION
%doc %{rlibdir}/MAINT.Data/html
%{rlibdir}/MAINT.Data/NAMESPACE
%{rlibdir}/MAINT.Data/help
%{rlibdir}/MAINT.Data/Meta
%{rlibdir}/MAINT.Data/INDEX
%{rlibdir}/MAINT.Data/data
%{rlibdir}/MAINT.Data/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora