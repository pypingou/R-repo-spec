%global packname  HistData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.12
Release:          1%{?dist}
Summary:          Data sets from the history of statistics and data visualization

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The HistData package provides a collection of small data sets that are
interesting and important in the history of statistics and data
visualization. The goal of the package is to make these available, both
for instructional use and for historical research.  Some of these present
interesting challenges for graphics or analysis in R.

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
%doc %{rlibdir}/HistData/NEWS
%doc %{rlibdir}/HistData/DESCRIPTION
%doc %{rlibdir}/HistData/html
%{rlibdir}/HistData/data
%{rlibdir}/HistData/INDEX
%{rlibdir}/HistData/help
%{rlibdir}/HistData/NAMESPACE
%{rlibdir}/HistData/Meta
%{rlibdir}/HistData/images

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.12-1
- initial package for Fedora