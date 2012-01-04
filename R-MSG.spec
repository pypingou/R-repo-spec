%global packname  MSG
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Data and functions for the book Modern Statistical Graphics

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-RColorBrewer 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-RColorBrewer 


%description
A companion to the Chinese book ``Modern Statistical Graphics'' by Yihui

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
%doc %{rlibdir}/MSG/html
%doc %{rlibdir}/MSG/NEWS
%doc %{rlibdir}/MSG/DESCRIPTION
%{rlibdir}/MSG/demo
%{rlibdir}/MSG/Meta
%{rlibdir}/MSG/data
%{rlibdir}/MSG/NAMESPACE
%{rlibdir}/MSG/R
%{rlibdir}/MSG/help
%{rlibdir}/MSG/extdata
%{rlibdir}/MSG/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora