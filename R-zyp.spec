%global packname  zyp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Zhang + Yue-Pilon trends package

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Kendall 

BuildRequires:    R-devel tex(latex) R-Kendall 

%description
The zyp package contains an efficient implementation of Sen's slope method
plus implementation of Xuebin Zhang's (Zhang, 1999) and Yue-Pilon's (Yue,
2002) prewhitening approaches to determining trends in climate data.

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
%doc %{rlibdir}/zyp/html
%doc %{rlibdir}/zyp/DESCRIPTION
%{rlibdir}/zyp/INDEX
%{rlibdir}/zyp/help
%{rlibdir}/zyp/Meta
%{rlibdir}/zyp/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora