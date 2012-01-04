%global packname  HFWutils
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.5.2011.03.21
Release:          1%{?dist}
Summary:          csv import, csv export, garbage collection,string matching and passing by reference

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-debug R-grDevices R-methods R-R.oo 

BuildRequires:    R-devel tex(latex) R-debug R-grDevices R-methods R-R.oo 

%description
package containing functions for convenient csv import and export with a
view of using R as a calculation back end to spreadsheet-like programs
such as scalc in open office; string matching and passing by reference

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
%doc %{rlibdir}/HFWutils/html
%doc %{rlibdir}/HFWutils/DESCRIPTION
%{rlibdir}/HFWutils/data
%{rlibdir}/HFWutils/help
%{rlibdir}/HFWutils/INDEX
%{rlibdir}/HFWutils/NAMESPACE
%{rlibdir}/HFWutils/Meta
%{rlibdir}/HFWutils/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.5.2011.03.21-1
- initial package for Fedora