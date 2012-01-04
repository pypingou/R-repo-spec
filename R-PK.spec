%global packname  PK
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Basic Non-Compartmental Pharmacokinetics

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Estimation of pharmacokinetic parameters using non-compartmental theory

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
%doc %{rlibdir}/PK/html
%doc %{rlibdir}/PK/NEWS
%doc %{rlibdir}/PK/CITATION
%doc %{rlibdir}/PK/DESCRIPTION
%{rlibdir}/PK/R
%{rlibdir}/PK/data
%{rlibdir}/PK/Meta
%{rlibdir}/PK/INDEX
%{rlibdir}/PK/NAMESPACE
%{rlibdir}/PK/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora