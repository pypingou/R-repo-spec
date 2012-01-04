%global packname  RthroughExcelWorkbooksInstaller
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          Excel Workbooks supporting Statistics courses using 'R through Excel'

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rcom R-HH 
Requires:         R-RExcelInstaller 

BuildRequires:    R-devel tex(latex) R-rcom R-HH
BuildRequires:    R-RExcelInstaller 


%description
Workbooks in Excel that illustrate statistical concepts by accessing R
functions from Excel.  These workbooks use the automatic recalculation
mode of Excel to update calculations and graphs in R.  This R package
downloads an executable which installs the workbooks on MS Windows systems
where RExcel has already been installed.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.6-1
- initial package for Fedora