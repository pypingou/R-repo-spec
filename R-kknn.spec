%global packname  kknn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Weighted k-Nearest Neighbors

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Matrix R-igraph 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Matrix R-igraph 


%description
Weighted k-Nearest Neighbors Classification, Regression and Clustering

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
%doc %{rlibdir}/kknn/html
%doc %{rlibdir}/kknn/DESCRIPTION
%doc %{rlibdir}/kknn/NEWS
%{rlibdir}/kknn/help
%{rlibdir}/kknn/INDEX
%{rlibdir}/kknn/libs
%{rlibdir}/kknn/Meta
%{rlibdir}/kknn/data
%{rlibdir}/kknn/R
%{rlibdir}/kknn/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora