%global packname  RExcelInstaller
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2.1.1
Release:          1%{?dist}
Summary:          Integration of R and Excel, (use R in Excel, read/write XLS files)

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.2.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rcom 


BuildRequires:    R-devel tex(latex) R-rcom



%description
RExcel, an add-in for MS Excel on MS Windows, allows to transfer data
between R and Excel, writing VBA macros using R as a library for Excel,
and calling R functions as worksheet function in Excel. RExcel integrates
nicely with R Commander (Rcmdr). This R package installs the Excel add-in
for Excel versions from 2003 to 2010. It only works on MS Windows.
RExcelInstaller installs RExcel for all supported versions of Excel found
on the target machine. The LGPL license only applies to the installer, not
to the Excel addin it installs.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.1.1-1
- initial package for Fedora