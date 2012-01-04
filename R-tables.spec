%global packname  tables
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Formula-driven table generation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Hmisc 


BuildRequires:    R-devel tex(latex) R-Hmisc



%description
Computes and displays complex tables of summary statistics

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
%doc %{rlibdir}/tables/DESCRIPTION
%doc %{rlibdir}/tables/html
%doc %{rlibdir}/tables/NEWS
%doc %{rlibdir}/tables/doc
%{rlibdir}/tables/INDEX
%{rlibdir}/tables/NAMESPACE
%{rlibdir}/tables/Meta
%{rlibdir}/tables/R
RPM build errors:
%{rlibdir}/tables/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora