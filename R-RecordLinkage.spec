%global packname  RecordLinkage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Record Linkage in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-e1071 R-rpart R-ada R-ipred R-stats R-evd R-RSQLite R-methods R-data.table 

BuildRequires:    R-devel tex(latex) R-e1071 R-rpart R-ada R-ipred R-stats R-evd R-RSQLite R-methods R-data.table 

%description
Provides functions for linking and deduplicating data sets. Methods based
on a stochastical approach are implemented as well as classification
algorithms from the machine learning domain.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora