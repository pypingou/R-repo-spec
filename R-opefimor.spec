%global packname  opefimor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Option Pricing and Estimation of Financial Models in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Companion package to the book Option Pricing and Estimation of Financial
Models in R, Wiley, Chichester. ISBN: 978-0-470-74584-7

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
%doc %{rlibdir}/opefimor/doc
%doc %{rlibdir}/opefimor/html
%doc %{rlibdir}/opefimor/DESCRIPTION
%{rlibdir}/opefimor/R
%{rlibdir}/opefimor/Meta
%{rlibdir}/opefimor/NAMESPACE
%{rlibdir}/opefimor/help
%{rlibdir}/opefimor/book
%{rlibdir}/opefimor/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora