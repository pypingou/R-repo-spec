%global packname  DTDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Doubly truncated data analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements different algorithms for analyzing randomly
truncated data, one-sided and two-sided (i.e. doubly) truncated data. Two
real data sets are included.

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
%doc %{rlibdir}/DTDA/html
%doc %{rlibdir}/DTDA/DESCRIPTION
%doc %{rlibdir}/DTDA/CITATION
%{rlibdir}/DTDA/R
%{rlibdir}/DTDA/data
%{rlibdir}/DTDA/INDEX
%{rlibdir}/DTDA/Meta
%{rlibdir}/DTDA/help
%{rlibdir}/DTDA/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.1-1
- initial package for Fedora