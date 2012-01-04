%global packname  RHRV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.5.1
Release:          1%{?dist}
Summary:          Heart rate variability analysis of ECG data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-tkrplot 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot 

%description
This is a package for developing heart rate variability studies of ECG

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
%doc %{rlibdir}/RHRV/DESCRIPTION
%doc %{rlibdir}/RHRV/html
%{rlibdir}/RHRV/help
%{rlibdir}/RHRV/Meta
%{rlibdir}/RHRV/R
%{rlibdir}/RHRV/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.5.1-1
- initial package for Fedora