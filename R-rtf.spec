%global packname  rtf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Rich Text Format (RTF) Output

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
A set of R functions to output Rich Text Format (RTF) files with high
resolution tables and graphics that may be edited with a standard word
processor such as Microsoft Word.

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
%doc %{rlibdir}/rtf/html
%doc %{rlibdir}/rtf/NEWS
%doc %{rlibdir}/rtf/DESCRIPTION
%{rlibdir}/rtf/NAMESPACE
%{rlibdir}/rtf/LICENSE
%{rlibdir}/rtf/Meta
%{rlibdir}/rtf/INDEX
%{rlibdir}/rtf/R
%{rlibdir}/rtf/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.3-1
- initial package for Fedora