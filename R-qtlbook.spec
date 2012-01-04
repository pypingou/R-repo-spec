%global packname  qtlbook
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.17.3
Release:          1%{?dist}
Summary:          Datasets for the R/qtl book

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.17-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-qtl 

BuildRequires:    R-devel tex(latex) R-qtl 

%description
Datasets for the book, A Guide to QTL Mapping with R/qtl

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
%doc %{rlibdir}/qtlbook/CITATION
%doc %{rlibdir}/qtlbook/html
%doc %{rlibdir}/qtlbook/DESCRIPTION
%{rlibdir}/qtlbook/STATUS.txt
%{rlibdir}/qtlbook/Meta
%{rlibdir}/qtlbook/data
%{rlibdir}/qtlbook/INDEX
%{rlibdir}/qtlbook/LICENSE.txt
%{rlibdir}/qtlbook/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.17.3-1
- initial package for Fedora