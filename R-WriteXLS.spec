%global packname  WriteXLS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Cross-platform Perl based R function to create Excel 2003 (XLS) files

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Cross-platform Perl based R function to create Excel 2003 (XLS) files from
one or more data frames. Each data frame will be written to a separate
named worksheet in the Excel spreadsheet. The worksheet name will be the
name of the data frame it contains or can be specified by the user.

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
%doc %{rlibdir}/WriteXLS/COPYING
%doc %{rlibdir}/WriteXLS/html
%doc %{rlibdir}/WriteXLS/DESCRIPTION
%{rlibdir}/WriteXLS/Meta
%{rlibdir}/WriteXLS/INDEX
%{rlibdir}/WriteXLS/help
%{rlibdir}/WriteXLS/INSTALL
%{rlibdir}/WriteXLS/Perl
%{rlibdir}/WriteXLS/R
%{rlibdir}/WriteXLS/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora