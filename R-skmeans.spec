%global packname  skmeans
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Spherical k-Means Clustering

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-slam R-clue R-cluster 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-slam R-clue R-cluster 


%description
Algorithms to compute spherical k-means partitions. Features several
methods, including a genetic and a fixed-point algorithm and an interface
to the CLUTO vcluster program.

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
%doc %{rlibdir}/skmeans/DESCRIPTION
%doc %{rlibdir}/skmeans/html
%{rlibdir}/skmeans/help
%{rlibdir}/skmeans/cluto
%{rlibdir}/skmeans/Meta
%{rlibdir}/skmeans/INDEX
%{rlibdir}/skmeans/R
%{rlibdir}/skmeans/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora