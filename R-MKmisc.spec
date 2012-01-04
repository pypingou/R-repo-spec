%global packname  MKmisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Miscellaneous Functions from M. Kohl

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics R-robustbase R-RColorBrewer 


BuildRequires:    R-devel tex(latex) R-stats R-graphics R-robustbase R-RColorBrewer



%description
Miscellaneous Functions from M. Kohl

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
%doc %{rlibdir}/MKmisc/html
%doc %{rlibdir}/MKmisc/DESCRIPTION
%doc %{rlibdir}/MKmisc/NEWS
%doc %{rlibdir}/MKmisc/CITATION
%{rlibdir}/MKmisc/R
%{rlibdir}/MKmisc/Meta
%{rlibdir}/MKmisc/help
%{rlibdir}/MKmisc/INDEX
%{rlibdir}/MKmisc/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora