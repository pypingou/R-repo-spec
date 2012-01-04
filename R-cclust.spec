%global packname  cclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.16
Release:          1%{?dist}
Summary:          Convex Clustering Methods and Clustering Indexes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-16.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Convex Clustering methods, including Kmeans algorithm, On-line Update
algorithm (Hard Competitive Learning) and Neural Gas algorithm (Soft
Competitive Learning) and calculation of several indexes for finding the
number of clusters in a data set.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.16-1
- initial package for Fedora